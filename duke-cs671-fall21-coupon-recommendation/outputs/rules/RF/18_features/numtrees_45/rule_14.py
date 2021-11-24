def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[12]>0.0:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[15]>-1.0:
				return 'False'
			elif obj[15]<=-1.0:
				return 'True'
			else: return 'True'
		elif obj[12]<=0.0:
			# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[6]>3:
				return 'True'
			elif obj[6]<=3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>1:
		# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[9]>0:
			return 'True'
		elif obj[9]<=0:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
