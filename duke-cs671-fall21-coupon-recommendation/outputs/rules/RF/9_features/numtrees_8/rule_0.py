def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9671, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 109, "metric_value": 0.9152, "depth": 2}
		if obj[4]<=20.61825381171262:
			# {"feature": "Restaurant20to50", "instances": 102, "metric_value": 0.9367, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Time", "instances": 66, "metric_value": 0.9894, "depth": 4}
				if obj[1]>0:
					# {"feature": "Bar", "instances": 49, "metric_value": 0.9997, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Direction_same", "instances": 28, "metric_value": 0.9403, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Passanger", "instances": 21, "metric_value": 0.8631, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[8]>1:
										return 'False'
									elif obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[8]>1:
									# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3]<=2:
										return 'True'
									elif obj[3]>2:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[7]>0:
							# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[3]>2:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[3]<=2:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=0.0:
						# {"feature": "Passanger", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							# {"feature": "Direction_same", "instances": 19, "metric_value": 0.8997, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.7793, "depth": 9}
									if obj[8]>1:
										return 'True'
									elif obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'False'
									elif obj[8]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>0:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>2:
									return 'True'
								elif obj[3]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]<=0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Bar", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 6}
						if obj[3]>0:
							# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>2.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>1.0:
				# {"feature": "Education", "instances": 36, "metric_value": 0.7107, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Time", "instances": 24, "metric_value": 0.4138, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[0]>2:
							# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[8]>1:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]>0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[5]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[8]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]<=2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>2:
					# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]<=3.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'False'
									else: return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>3.0:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>20.61825381171262:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Bar", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[5]<=1.0:
			return 'False'
		elif obj[5]>1.0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[4]>5:
				return 'True'
			elif obj[4]<=5:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
