def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[4]>0:
		# {"feature": "Gender", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[3]>0:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[13]<=2:
					return 'True'
				elif obj[13]>2:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[13]<=2:
				# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[7]>5:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[7]<=5:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]<=0:
		return 'False'
	else: return 'False'
