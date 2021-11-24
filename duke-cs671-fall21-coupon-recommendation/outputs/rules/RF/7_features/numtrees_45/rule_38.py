def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=12:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>1.0:
				# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[3]>12:
		return 'False'
	else: return 'False'
