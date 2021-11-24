def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[12]<=1:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]>1:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[7]>4:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								return 'False'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[7]<=4:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[12]>1:
				return 'False'
			else: return 'False'
		elif obj[10]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[10]>0.0:
			return 'True'
		elif obj[10]<=0.0:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
