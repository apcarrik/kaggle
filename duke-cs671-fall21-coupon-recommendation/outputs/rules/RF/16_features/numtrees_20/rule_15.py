def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.874, "depth": 1}
	if obj[9]<=7:
		# {"feature": "Education", "instances": 32, "metric_value": 0.5436, "depth": 2}
		if obj[8]<=1:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Time", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[0]>0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>3:
				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>1:
			return 'True'
		else: return 'True'
	elif obj[9]>7:
		# {"feature": "Bar", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[11]<=1.0:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[15]<=1:
				# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]>1:
						return 'True'
					elif obj[3]<=1:
						return 'False'
					else: return 'False'
				elif obj[7]>0:
					return 'False'
				else: return 'False'
			elif obj[15]>1:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[8]>0:
					return 'True'
				elif obj[8]<=0:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[11]>1.0:
			return 'False'
		else: return 'False'
	else: return 'False'
