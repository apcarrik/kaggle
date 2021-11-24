def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[2]>0:
		# {"feature": "Time", "instances": 41, "metric_value": 0.839, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Education", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[8]<=1:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>6:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=6:
							return 'False'
						else: return 'False'
					elif obj[8]>1:
						return 'True'
					else: return 'True'
				elif obj[5]>0.0:
					return 'True'
				else: return 'True'
			elif obj[3]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]<=2.0:
						return 'False'
					elif obj[5]>2.0:
						return 'True'
					else: return 'True'
				elif obj[6]<=0.0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=7:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>7:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>1:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[5]<=2.0:
				return 'True'
			elif obj[5]>2.0:
				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[5]<=0.0:
			return 'False'
		elif obj[5]>0.0:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=0:
					return 'False'
				elif obj[7]>0:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
