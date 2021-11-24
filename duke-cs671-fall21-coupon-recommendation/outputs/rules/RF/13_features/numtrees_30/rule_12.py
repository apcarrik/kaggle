def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Passanger", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[6]<=4:
				# {"feature": "Time", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[12]<=1:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[7]>1:
							return 'False'
						elif obj[7]<=1:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>4:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[12]>1:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			elif obj[10]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>4:
		# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[7]<=12:
			return 'True'
		elif obj[7]>12:
			return 'False'
		else: return 'False'
	else: return 'True'
