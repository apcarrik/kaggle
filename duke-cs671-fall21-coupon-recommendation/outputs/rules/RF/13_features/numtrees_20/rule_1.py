def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[6]>0:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[7]>7:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[12]<=2:
								return 'False'
							elif obj[12]>2:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				elif obj[7]<=7:
					return 'True'
				else: return 'True'
			elif obj[9]>2.0:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[10]>0.0:
					return 'False'
				elif obj[10]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]<=0:
		# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[9]>0.0:
			return 'True'
		elif obj[9]<=0.0:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]>0:
					return 'True'
				elif obj[7]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
