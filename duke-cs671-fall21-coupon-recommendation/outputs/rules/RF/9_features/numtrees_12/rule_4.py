def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 67, "metric_value": 0.8971, "depth": 2}
		if obj[4]<=7:
			# {"feature": "Education", "instances": 43, "metric_value": 0.7401, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.5917, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Distance", "instances": 32, "metric_value": 0.4489, "depth": 5}
					if obj[8]>1:
						# {"feature": "Time", "instances": 19, "metric_value": 0.6292, "depth": 6}
						if obj[1]>0:
							# {"feature": "Bar", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]>2:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>2.0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				elif obj[6]<=0.0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>2:
				# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>7:
			# {"feature": "Distance", "instances": 24, "metric_value": 1.0, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Time", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]>0:
									return 'False'
								elif obj[7]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[3]>0:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[5]>0.0:
							return 'False'
						elif obj[5]<=0.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[5]>0.0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=6:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]<=0:
								return 'True'
							elif obj[7]>0:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]>6:
						return 'False'
					else: return 'False'
				elif obj[3]>3:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[5]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
