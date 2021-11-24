def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[9]<=1.0:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.7579, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Bar", "instances": 25, "metric_value": 0.5294, "depth": 3}
			if obj[7]<=0.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[6]>5:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[8]>0.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=5:
					return 'True'
				else: return 'True'
			elif obj[7]>0.0:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=20:
					return 'True'
				elif obj[6]>20:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[9]>1.0:
		# {"feature": "Time", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[6]>4:
					return 'False'
				elif obj[6]<=4:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>2:
						return 'False'
					elif obj[4]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>2:
				# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[11]<=2:
					return 'False'
				elif obj[11]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
