def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[13]>1:
		# {"feature": "Occupation", "instances": 27, "metric_value": 0.8256, "depth": 2}
		if obj[7]>7:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[8]<=5:
							return 'False'
						elif obj[8]>5:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>1:
								return 'False'
							elif obj[1]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[7]<=7:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[9]<=1.0:
				return 'False'
			elif obj[9]>1.0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[13]<=1:
		# {"feature": "Income", "instances": 24, "metric_value": 0.7383, "depth": 2}
		if obj[8]>1:
			# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[10]>0.0:
				return 'True'
			elif obj[10]<=0.0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[7]<=5:
					return 'True'
				elif obj[7]>5:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]>0.0:
						return 'False'
					elif obj[11]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[8]<=1:
			# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[5]>0:
				return 'False'
			elif obj[5]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
