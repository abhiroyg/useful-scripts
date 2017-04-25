#include <stdio.h>
#include <stdlib.h>

struct node {
    char *data;
    struct node *next;
};

int main(void) {
    struct node *head = NULL;
    struct node *temp = (struct node*) malloc(sizeof(char)*256);
    printf("%lu\n", sizeof(*temp));
    temp->data = "haha";
    temp->next = NULL;
    head = temp;
    printf("%lu\n", sizeof(*temp));

    struct node *temp1 = (struct node*) malloc(sizeof(char)*256);
    printf("%lu\n", sizeof(*temp1));
    temp1->data = "hehealskdjflaskdfjlasdkfjalsdkjflaskdjflaksdjflaksjdflasjdflakjsdlfkajsdflkajsdlfkjalsdkfjalskdjflaksdjflaksjdflakjsdlfkajsdlkfajsdlfkjalsdkfjalskdfjlaksdjflaksjdflkasjfdlkasjdflkajsdlfkajsdlkfjalsdkfjalksdfjlaksdjflaksdjflaksdjflakjsdflkajsdflkajsdlfkjasdlkfjasldkfjalkdsjflaksdfjlaksdjflksdjflakdsjflakdsjflaksjdflkasdjflkasjdflkajdsflkajsdlfkjasldfkjsaldkfjalskdfjlaskdfjlaskdfj";
    temp1->next = NULL;
    head->next = temp1;
    printf("%lu\n", sizeof(*temp1));

    printf("%s -> %s\n", head->data, head->next->data);

    head = head->next;
    free(temp);

    printf("%s\n", head->data);

    head = head->next;
    free(temp1);

    printf("%d\n", head);
}
