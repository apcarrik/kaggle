def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Age", "instances": 33, "metric_value": 0.9183, "depth": 2}
		if obj[4]>0:
			# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[9]>1.0:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[7]>5:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[11]<=0:
						# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]<=0:
									return 'False'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]>2.0:
							return 'True'
						else: return 'True'
					elif obj[11]>0:
						return 'True'
					else: return 'True'
				elif obj[7]<=5:
					# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[8]>0.0:
						return 'True'
					elif obj[8]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=1.0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[7]>1:
					return 'False'
				elif obj[7]<=1:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Age", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[4]<=2:
			return 'True'
		elif obj[4]>2:
			# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=7:
					return 'True'
				elif obj[7]>7:
					return 'False'
				else: return 'False'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
