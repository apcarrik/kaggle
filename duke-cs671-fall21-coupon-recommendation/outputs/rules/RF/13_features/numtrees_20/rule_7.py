def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[12]<=2:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.8673, "depth": 2}
		if obj[7]>1:
			# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.9183, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Passanger", "instances": 28, "metric_value": 0.9852, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[9]<=3.0:
						# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[1]>0:
							# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[4]<=4:
								return 'False'
							elif obj[4]>4:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=0:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]>0:
								# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[9]>3.0:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>1.0:
				# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=1:
			return 'True'
		else: return 'True'
	elif obj[12]>2:
		return 'False'
	else: return 'False'
