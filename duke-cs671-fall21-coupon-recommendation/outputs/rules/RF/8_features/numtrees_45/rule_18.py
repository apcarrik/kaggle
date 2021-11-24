def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[3]>1:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=0.0:
					return 'False'
				elif obj[4]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[2]<=0:
			# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[4]<=0.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=5:
						return 'True'
					elif obj[3]>5:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[4]>0.0:
				return 'False'
			else: return 'False'
		elif obj[2]>0:
			return 'True'
		else: return 'True'
	else: return 'True'
