def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[8]<=2:
		# {"feature": "Coupon", "instances": 76, "metric_value": 0.9387, "depth": 2}
		if obj[2]>1:
			# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.8315, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Bar", "instances": 46, "metric_value": 0.9109, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Occupation", "instances": 34, "metric_value": 0.7871, "depth": 5}
					if obj[4]<=7:
						# {"feature": "Time", "instances": 29, "metric_value": 0.8498, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 7}
							if obj[3]<=1:
								# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[3]>1:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>1:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[0]>0:
								# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[0]<=0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=2:
									return 'True'
								elif obj[3]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[4]>7:
						return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[7]<=0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=12:
								# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[4]>12:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=12:
								return 'True'
							elif obj[4]>12:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[7]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[4]>3:
						# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=1.0:
								return 'True'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						elif obj[7]>0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]<=3:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>2:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]>2:
		return 'False'
	else: return 'False'
