def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[2]>1:
			# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=14:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1.0:
						return 'True'
					elif obj[4]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]>14:
					return 'False'
				else: return 'False'
			elif obj[5]>2:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=10:
					return 'False'
				elif obj[3]>10:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>1.0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[3]>2:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=1:
					return 'False'
				elif obj[5]>1:
					return 'True'
				else: return 'True'
			elif obj[3]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
