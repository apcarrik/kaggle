def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[8]>1:
		# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[0]>1:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]>2:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]>6:
						return 'False'
					elif obj[4]<=6:
						return 'True'
					else: return 'True'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			return 'True'
		else: return 'True'
	elif obj[8]<=1:
		return 'True'
	else: return 'True'
