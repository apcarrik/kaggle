def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Bar", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[4]>0.0:
		# {"feature": "Education", "instances": 50, "metric_value": 0.9896, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[3]>1:
				# {"feature": "Direction_same", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[7]>1:
						# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[1]>1:
							# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]>1.0:
									return 'False'
								elif obj[5]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]>0:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[7]<=1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]>2:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						elif obj[1]<=2:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>1.0:
								return 'False'
							elif obj[5]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[3]<=22:
				# {"feature": "Direction_same", "instances": 20, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Distance", "instances": 19, "metric_value": 0.7425, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Coupon", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[0]>1:
									return 'True'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[7]>2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]>0:
					return 'False'
				else: return 'False'
			elif obj[3]>22:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]<=0.0:
		# {"feature": "Coupon", "instances": 35, "metric_value": 0.9275, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.9852, "depth": 3}
			if obj[3]>1:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Distance", "instances": 20, "metric_value": 0.9928, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Passanger", "instances": 18, "metric_value": 0.9641, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]>0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[7]>2:
						return 'True'
					else: return 'True'
				elif obj[5]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
