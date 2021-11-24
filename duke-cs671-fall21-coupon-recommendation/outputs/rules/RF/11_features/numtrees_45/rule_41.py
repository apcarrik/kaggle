def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]>1:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[2]>2:
			# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0.0:
						return 'True'
					elif obj[6]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		elif obj[2]<=2:
			return 'False'
		else: return 'False'
	elif obj[10]<=1:
		return 'True'
	else: return 'True'
