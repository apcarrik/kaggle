def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Time", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[4]<=5:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>5:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[4]<=10:
				return 'True'
			elif obj[4]>10:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]>2:
		return 'False'
	else: return 'False'
