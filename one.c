#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

struct frag {
        char data[5];
        int len;
        struct frag *next;
};

static unsigned char S[256];

void
swap(unsigned char *a, unsigned char *b)
{
        unsigned char c;
        c = *a;
        *a = *b;
        *b = c;
}

void
cipher_init(char *key, int keylen)
{
        int i, j;
        for (i = 0; i < 256; ++i)
                S[i] = i;
        j = 0;
        for (i = 0; i < 256; ++i) {
                j = (j + S[i] + key[i % keylen]) % 256;
                swap(S+i, S+j);
        }
}

unsigned char
cipher_next()
{
        static int i = 0;
        static int j = 0;
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        swap(S+i, S+j);
        return S[(S[i] + S[j]) % 256];
}

struct frag *
frag_alloc()
{
        return calloc(1, sizeof(struct frag));
}

struct frag *
read_input()
{
        struct frag *cur, *head;
        char c;

        head = cur = frag_alloc();
        while (1) {
		printf("Give input: ");
                ssize_t nr = read(0, &c, 1);
		printf("\nRead %c\n", c);
                putchar((char)nr);
		if (nr < 0)
                        return head;
                if (nr == 0)
                        break;
                cur->data[cur->len++] = c ^ cipher_next();
                if (cur->len == sizeof(cur->data)) {
                        cur->next = frag_alloc();
                        cur = cur->next;
                }
        }
        return head;
}

void
frag_dump(struct frag *f)
{
        int i;
        while (f != NULL && f->len) {
                for (i = 0; i < f->len; ++i)
                        putchar(f->data[i]);
                f = f->next;
        }
}

int main()
{
        struct frag *f;
	printf("Init cipher\n");
        cipher_init("gQ90YiaJcd2Kfq59", strlen("gQ90YiaJcd2Kfq59"));
        printf("Starting to read input\n");
	f = read_input();
	printf("Dumping cipher\n");
        frag_dump(f);
        return 0;
}
