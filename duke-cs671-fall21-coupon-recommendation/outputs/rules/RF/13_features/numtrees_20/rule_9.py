def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[7]>4:
		# {"feature": "Age", "instances": 38, "metric_value": 0.9819, "depth": 2}
		if obj[4]>0:
			# {"feature": "Coupon", "instances": 30, "metric_value": 0.9968, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[8]<=3.0:
						# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[9]>0.0:
							return 'True'
						elif obj[9]<=0.0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]>3.0:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[10]<=1.0:
						return 'False'
					elif obj[10]>1.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[7]<=4:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[2]>0:
			return 'True'
		elif obj[2]<=0:
			# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
