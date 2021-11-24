def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Children", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[11]<=0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1:
							return 'True'
						elif obj[4]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]>0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[7]>6:
						return 'True'
					elif obj[7]<=6:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2:
				return 'True'
			else: return 'True'
		elif obj[5]>0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[7]<=7:
			return 'True'
		elif obj[7]>7:
			return 'False'
		else: return 'False'
	else: return 'True'
