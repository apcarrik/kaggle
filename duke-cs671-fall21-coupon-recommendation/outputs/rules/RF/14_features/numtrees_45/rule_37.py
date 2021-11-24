def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[9]<=0.0:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[2]>0:
			# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[4]<=6:
					return 'False'
				elif obj[4]>6:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[9]>0.0:
		return 'True'
	else: return 'True'
