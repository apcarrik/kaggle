def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[10]<=7:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[3]>0:
			# {"feature": "Income", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[11]<=6:
				return 'True'
			elif obj[11]>6:
				return 'False'
			else: return 'False'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	elif obj[10]>7:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[9]>0:
			return 'False'
		elif obj[9]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
