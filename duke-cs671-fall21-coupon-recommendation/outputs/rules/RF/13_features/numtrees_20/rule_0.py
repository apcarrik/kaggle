def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[6]>0:
		# {"feature": "Age", "instances": 34, "metric_value": 0.99, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.8113, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[1]>0:
							# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[3]>0:
								# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]>0:
									return 'False'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[9]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[4]>3:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[7]>5:
				# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[10]>0.0:
						return 'True'
					elif obj[10]<=0.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[9]>1.0:
					return 'False'
				else: return 'False'
			elif obj[7]<=5:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[6]<=0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
