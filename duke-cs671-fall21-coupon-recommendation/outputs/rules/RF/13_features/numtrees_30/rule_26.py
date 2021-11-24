def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.9044, "depth": 2}
		if obj[7]<=8:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Children", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]>2:
				return 'True'
			else: return 'True'
		elif obj[7]>8:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[10]<=2.0:
				return 'False'
			elif obj[10]>2.0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
