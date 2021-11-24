def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Time", "instances": 127, "metric_value": 0.9996, "depth": 1}
	if obj[1]>1:
		# {"feature": "Education", "instances": 75, "metric_value": 0.9427, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Bar", "instances": 55, "metric_value": 0.8184, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Income", "instances": 33, "metric_value": 0.9457, "depth": 4}
				if obj[8]<=5:
					# {"feature": "Occupation", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[7]<=7:
						# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[13]>1:
								# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[10]>-1.0:
									return 'False'
								elif obj[10]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[13]<=1:
								return 'True'
							else: return 'True'
						elif obj[4]>3:
							return 'True'
						else: return 'True'
					elif obj[7]>7:
						return 'False'
					else: return 'False'
				elif obj[8]>5:
					return 'True'
				else: return 'True'
			elif obj[9]>1.0:
				# {"feature": "Coupon", "instances": 22, "metric_value": 0.4395, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Age", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[4]>0:
				# {"feature": "Passanger", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[0]>1:
					# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[5]>0:
						# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=12:
								return 'True'
							elif obj[7]>12:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Education", "instances": 52, "metric_value": 0.8404, "depth": 2}
		if obj[6]>1:
			# {"feature": "Passanger", "instances": 31, "metric_value": 0.6374, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Income", "instances": 30, "metric_value": 0.5665, "depth": 4}
				if obj[8]<=7:
					# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.4798, "depth": 5}
					if obj[11]>-1.0:
						# {"feature": "Occupation", "instances": 28, "metric_value": 0.3712, "depth": 6}
						if obj[7]>5:
							return 'False'
						elif obj[7]<=5:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[2]>1:
									return 'False'
								elif obj[2]<=1:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[9]>1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[8]>7:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[6]<=1:
			# {"feature": "Age", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[4]>0:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[12]<=0:
							return 'False'
						elif obj[12]>0:
							# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]>3:
								return 'True'
							elif obj[8]<=3:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[11]<=2.0:
						return 'False'
					elif obj[11]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
