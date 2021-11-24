def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[3]<=7:
			# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]<=2:
				return 'True'
			elif obj[2]>2:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>2:
					return 'True'
				elif obj[0]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>7:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]>1:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
