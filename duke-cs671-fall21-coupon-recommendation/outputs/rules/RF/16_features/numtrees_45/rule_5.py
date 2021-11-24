def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Income", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[10]>0:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[12]<=1.0:
				return 'False'
			elif obj[12]>1.0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]<=0:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
