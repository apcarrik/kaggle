def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[10]>4:
		# {"feature": "Age", "instances": 32, "metric_value": 0.9284, "depth": 2}
		if obj[6]<=6:
			# {"feature": "Income", "instances": 29, "metric_value": 0.9576, "depth": 3}
			if obj[11]>2:
				# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.8454, "depth": 4}
				if obj[7]<=1:
					# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[13]>-1.0:
						return 'False'
					elif obj[13]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[7]>1:
					# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[8]>0:
						# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[16]>1:
								return 'False'
							elif obj[16]<=1:
								return 'True'
							else: return 'True'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					elif obj[8]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[11]<=2:
				# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=3:
						return 'True'
					elif obj[3]>3:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>6:
			return 'False'
		else: return 'False'
	elif obj[10]<=4:
		# {"feature": "Age", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[6]>1:
			# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[12]<=1.0:
				# {"feature": "Weather", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Maritalstatus", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[7]>0:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[15]<=0:
							return 'False'
						elif obj[15]>0:
							return 'True'
						else: return 'True'
					elif obj[7]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			elif obj[12]>1.0:
				return 'True'
			else: return 'True'
		elif obj[6]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
