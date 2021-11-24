def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[4]>6:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=6:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[8]<=1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[8]>1:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>2:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]>6:
				return 'True'
			elif obj[4]<=6:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
