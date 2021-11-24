def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Age", "instances": 23, "metric_value": 0.7554, "depth": 2}
		if obj[4]>1:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[6]>1:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[7]<=1.0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[1]<=2:
							return 'True'
						elif obj[1]>2:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>1.0:
						# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]>1.0:
								return 'False'
							elif obj[8]<=1.0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=1:
					return 'False'
				else: return 'False'
			elif obj[9]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
