def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[1]>1:
		# {"feature": "Passanger", "instances": 36, "metric_value": 0.8113, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 18, "metric_value": 0.5033, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[6]>1:
						return 'True'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					return 'False'
				else: return 'False'
			elif obj[2]>0:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]<=12:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[3]>12:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[6]>1:
			# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>5:
					return 'True'
				elif obj[3]<=5:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]<=1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=2:
				return 'True'
			elif obj[2]>2:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>6:
					return 'True'
				elif obj[3]<=6:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'False'
