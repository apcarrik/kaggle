def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[6]<=1.0:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[4]<=8:
			# {"feature": "Time", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[2]>1:
					# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[8]<=1:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[8]>1:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>8:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[2]>2:
				return 'False'
			elif obj[2]<=2:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1.0:
						return 'False'
					elif obj[5]>1.0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>1.0:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[3]<=2:
			return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
