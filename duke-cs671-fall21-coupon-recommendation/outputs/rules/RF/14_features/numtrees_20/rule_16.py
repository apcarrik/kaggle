def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[2]>1:
		# {"feature": "Income", "instances": 30, "metric_value": 0.9481, "depth": 2}
		if obj[8]<=5:
			# {"feature": "Direction_same", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[12]<=0:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[7]>4:
					# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[7]<=4:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]>0:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>5:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[12]<=0:
			# {"feature": "Income", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[8]>3:
				# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[7]<=12:
					return 'False'
				elif obj[7]>12:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=0:
						return 'False'
					elif obj[0]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=3:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[10]>1.0:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[11]>0.0:
						return 'True'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[10]<=1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[12]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
