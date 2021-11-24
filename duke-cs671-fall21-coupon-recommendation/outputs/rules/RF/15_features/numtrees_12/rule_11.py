def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Bar", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[10]<=2.0:
		# {"feature": "Passanger", "instances": 73, "metric_value": 0.9999, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Direction_same", "instances": 45, "metric_value": 0.971, "depth": 3}
			if obj[13]<=0:
				# {"feature": "Income", "instances": 30, "metric_value": 0.7838, "depth": 4}
				if obj[9]<=4:
					# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Age", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[5]>2:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[12]<=1.0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[14]>1:
									return 'False'
								elif obj[14]<=1:
									return 'True'
								else: return 'True'
							elif obj[12]>1.0:
								return 'True'
							else: return 'True'
						elif obj[5]<=2:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[9]>4:
					return 'False'
				else: return 'False'
			elif obj[13]>0:
				# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=3:
							return 'True'
						elif obj[9]>3:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=5:
								return 'False'
							elif obj[5]>5:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Children", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[6]>0:
				# {"feature": "Time", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[7]>1:
						return 'True'
					elif obj[7]<=1:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=0:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[8]<=7:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[2]>1:
						# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[3]>0:
							# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]>1.0:
									return 'True'
								elif obj[11]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[8]>7:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[10]>2.0:
		# {"feature": "Age", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[5]<=6:
			# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[7]<=2:
				return 'True'
			elif obj[7]>2:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[5]>6:
			return 'False'
		else: return 'False'
	else: return 'True'
