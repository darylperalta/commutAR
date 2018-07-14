using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class OriginSelector : MonoBehaviour {

	public GameObject origin;
	public GameObject buttons;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if (GetComponent<DefaultTrackableEventHandler>().isTracked) {
			origin.GetComponent<Image>().enabled = true;
			origin.transform.GetChild(0).GetComponent<Image>().enabled = true;
			origin.transform.localPosition = new Vector3(buttons.transform.GetChild(transform.GetSiblingIndex()).localPosition.x, origin.transform.localPosition.y, 0f);
			//origin.transform.SetParent(buttons.transform.GetChild(transform.GetSiblingIndex()), false);
			origin.transform.parent = buttons.transform.GetChild(transform.GetSiblingIndex());
		}
	}
}
