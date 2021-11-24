def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[7]<=16:
		# {"feature": "Bar", "instances": 46, "metric_value": 0.9986, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Education", "instances": 25, "metric_value": 0.9427, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[10]>1.0:
					return 'True'
				elif obj[10]<=1.0:
					# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]>3:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]<=3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]>2:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[9]<=2.0:
					# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4]>0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[9]>2.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[8]<=0.0:
			# {"feature": "Passanger", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.8997, "depth": 4}
				if obj[2]>0:
					# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[4]>2:
						# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[9]<=0.0:
									return 'False'
								elif obj[9]>0.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>0:
							return 'False'
						else: return 'False'
					elif obj[4]<=2:
						# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]>0:
							return 'True'
						elif obj[5]<=0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>16:
		return 'True'
	else: return 'True'
