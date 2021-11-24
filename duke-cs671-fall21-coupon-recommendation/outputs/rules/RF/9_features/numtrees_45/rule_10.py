def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]<=0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[2]>0:
			# {"feature": "Time", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[6]>0.0:
					return 'True'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]>1:
						return 'True'
					elif obj[8]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]>5:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[7]>0:
		return 'False'
	else: return 'False'
