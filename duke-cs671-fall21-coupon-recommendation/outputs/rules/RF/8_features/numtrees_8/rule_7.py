def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Coupon", "instances": 116, "metric_value": 0.9862, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Bar", "instances": 75, "metric_value": 0.9311, "depth": 3}
			if obj[4]<=2.0:
				# {"feature": "Occupation", "instances": 69, "metric_value": 0.9558, "depth": 4}
				if obj[3]<=14:
					# {"feature": "Education", "instances": 60, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						# {"feature": "Passanger", "instances": 35, "metric_value": 0.971, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9799, "depth": 7}
							if obj[5]>-1.0:
								# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9656, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[5]<=-1.0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Passanger", "instances": 25, "metric_value": 0.795, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.5033, "depth": 7}
							if obj[5]>0.0:
								return 'True'
							elif obj[5]<=0.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[3]>14:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]>0.0:
							return 'False'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 41, "metric_value": 0.9789, "depth": 3}
			if obj[3]>4:
				# {"feature": "Education", "instances": 27, "metric_value": 0.7642, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.6343, "depth": 5}
					if obj[5]>-1.0:
						# {"feature": "Direction_same", "instances": 24, "metric_value": 0.5436, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Bar", "instances": 19, "metric_value": 0.6292, "depth": 7}
							if obj[4]>0.0:
								# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[4]<=0.0:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[5]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[3]<=4:
				# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[4]<=0.0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0.0:
						return 'False'
					elif obj[4]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[7]>2:
		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[5]<=1.0:
			return 'False'
		elif obj[5]>1.0:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
