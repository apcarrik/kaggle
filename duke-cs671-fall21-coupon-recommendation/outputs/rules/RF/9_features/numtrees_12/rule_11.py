def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 53, "metric_value": 0.9052, "depth": 2}
		if obj[3]>1:
			# {"feature": "Distance", "instances": 29, "metric_value": 0.9991, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.971, "depth": 4}
				if obj[4]<=19:
					# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.9024, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Direction_same", "instances": 19, "metric_value": 0.8315, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 8}
								if obj[1]>0:
									# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[5]<=2.0:
										return 'False'
									elif obj[5]>2.0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5]<=1.0:
										return 'True'
									elif obj[5]>1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>0:
								return 'True'
							else: return 'True'
						elif obj[6]<=0.0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								return 'False'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]>19:
					return 'False'
				else: return 'False'
			elif obj[8]>2:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Passanger", "instances": 24, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[4]>1:
					# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[5]<=1.0:
						return 'True'
					elif obj[5]>1.0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0.0:
						return 'False'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 32, "metric_value": 0.9544, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Direction_same", "instances": 21, "metric_value": 0.7025, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[4]<=10:
					return 'False'
				elif obj[4]>10:
					# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>1:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=2:
										return 'False'
									elif obj[8]>2:
										return 'True'
									else: return 'True'
								elif obj[3]<=1:
									return 'True'
								else: return 'True'
							elif obj[6]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[7]>0:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=1:
					return 'True'
				elif obj[8]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[5]>1.0:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[8]>1:
				# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=5:
						return 'True'
					elif obj[4]>5:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
