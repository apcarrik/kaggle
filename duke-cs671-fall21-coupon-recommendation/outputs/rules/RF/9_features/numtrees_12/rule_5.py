def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9259, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 56, "metric_value": 0.9991, "depth": 2}
		if obj[4]<=17:
			# {"feature": "Education", "instances": 46, "metric_value": 0.9781, "depth": 3}
			if obj[3]>1:
				# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.999, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Distance", "instances": 26, "metric_value": 0.9957, "depth": 5}
					if obj[8]<=2:
						# {"feature": "Time", "instances": 22, "metric_value": 0.976, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 7}
							if obj[2]>0:
								# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[5]>1.0:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						elif obj[1]>3:
							# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[2]>3:
									return 'True'
								elif obj[2]<=3:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>2:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=2.0:
							return 'True'
						elif obj[5]>2.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2.0:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.8315, "depth": 4}
				if obj[2]>0:
					# {"feature": "Bar", "instances": 16, "metric_value": 0.6962, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[8]<=2:
							return 'True'
						elif obj[8]>2:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=1.0:
						return 'False'
					elif obj[6]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[4]>17:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[8]<=2:
					return 'False'
				elif obj[8]>2:
					return 'True'
				else: return 'True'
			elif obj[6]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.3621, "depth": 2}
		if obj[2]>1:
			return 'True'
		elif obj[2]<=1:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]>2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
