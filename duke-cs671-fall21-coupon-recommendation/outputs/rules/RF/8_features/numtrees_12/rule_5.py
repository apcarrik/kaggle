def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[0]>0:
		# {"feature": "Coupon", "instances": 81, "metric_value": 0.9867, "depth": 2}
		if obj[1]>1:
			# {"feature": "Education", "instances": 58, "metric_value": 0.9444, "depth": 3}
			if obj[2]>1:
				# {"feature": "Bar", "instances": 29, "metric_value": 0.9991, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 5}
					if obj[3]<=16:
						# {"feature": "Direction_same", "instances": 18, "metric_value": 0.8524, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.7871, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Distance", "instances": 15, "metric_value": 0.8366, "depth": 8}
								if obj[7]>1:
									return 'True'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[5]>2.0:
								return 'True'
							else: return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[3]>16:
						return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[3]>5:
						return 'False'
					elif obj[3]<=5:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=1:
				# {"feature": "Occupation", "instances": 29, "metric_value": 0.7973, "depth": 4}
				if obj[3]<=11:
					# {"feature": "Bar", "instances": 18, "metric_value": 0.5033, "depth": 5}
					if obj[4]<=0.0:
						# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[4]>0.0:
						return 'True'
					else: return 'True'
				elif obj[3]>11:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2.0:
							return 'False'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]<=2.0:
							return 'True'
						elif obj[5]>2.0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]>1:
								return 'True'
							elif obj[7]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.8813, "depth": 4}
				if obj[7]>1:
					# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[3]<=10:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[2]<=1:
								return 'False'
							elif obj[2]>1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>1.0:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>10:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]<=1:
					return 'False'
				else: return 'False'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
