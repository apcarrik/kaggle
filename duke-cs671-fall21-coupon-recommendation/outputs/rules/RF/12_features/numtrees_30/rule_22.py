def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[4]>0:
		# {"feature": "Passanger", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[11]>2:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=11:
								return 'True'
							elif obj[6]>11:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[11]<=2:
						return 'False'
					else: return 'False'
				elif obj[9]>1.0:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=1:
							return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]>0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[4]<=0:
		return 'True'
	else: return 'True'
