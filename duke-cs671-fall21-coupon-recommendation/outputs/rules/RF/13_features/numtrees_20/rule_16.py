def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[7]<=21:
		# {"feature": "Passanger", "instances": 49, "metric_value": 0.9313, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Distance", "instances": 39, "metric_value": 0.9766, "depth": 3}
			if obj[12]>1:
				# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[2]>1:
								return 'False'
							elif obj[2]<=1:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3]>0:
									# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										return 'False'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[10]<=0.0:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=1.0:
								return 'False'
							elif obj[8]>1.0:
								return 'True'
							else: return 'True'
						elif obj[9]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>4:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[10]>0.0:
						return 'True'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[12]<=1:
				# {"feature": "Bar", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[8]<=3.0:
					# {"feature": "Time", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[11]<=0:
							# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[2]>0:
								return 'True'
							elif obj[2]<=0:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]>3.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>2:
					return 'False'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[7]>21:
		return 'False'
	else: return 'False'
