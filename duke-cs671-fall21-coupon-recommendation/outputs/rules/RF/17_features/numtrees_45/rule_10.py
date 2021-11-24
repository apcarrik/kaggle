def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[16]>1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[16]<=1:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[11]<=6:
			return 'False'
		elif obj[11]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
