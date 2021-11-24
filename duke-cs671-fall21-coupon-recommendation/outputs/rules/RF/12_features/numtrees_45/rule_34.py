def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>2:
		# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[11]<=1:
			# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=8:
					return 'False'
				elif obj[6]>8:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[11]>1:
			return 'False'
		else: return 'False'
	elif obj[2]<=2:
		# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[11]<=2:
			return 'True'
		elif obj[11]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
