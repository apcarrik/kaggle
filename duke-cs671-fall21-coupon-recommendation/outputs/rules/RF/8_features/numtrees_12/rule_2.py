def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[1]>1:
		# {"feature": "Direction_same", "instances": 68, "metric_value": 0.8918, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Passanger", "instances": 50, "metric_value": 0.958, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 32, "metric_value": 0.9972, "depth": 4}
				if obj[3]>5:
					# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Bar", "instances": 20, "metric_value": 1.0, "depth": 6}
						if obj[4]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.998, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Distance", "instances": 18, "metric_value": 0.9911, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									return 'False'
								else: return 'False'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[4]>3.0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[3]<=5:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[3]>1:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[7]>1:
						# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2]>0:
							# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5]>0.0:
									return 'True'
								elif obj[5]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[7]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=1:
						return 'False'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Bar", "instances": 18, "metric_value": 0.5033, "depth": 3}
			if obj[4]<=3.0:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.3228, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]<=1.0:
						return 'True'
					elif obj[5]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>3.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Bar", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[3]<=22:
				# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]>0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]>1:
									return 'False'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>2.0:
						return 'True'
					else: return 'True'
				elif obj[6]>0:
					return 'False'
				else: return 'False'
			elif obj[3]>22:
				return 'True'
			else: return 'True'
		elif obj[4]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
