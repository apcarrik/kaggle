def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[10]>0.0:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.9957, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[7]<=9:
				# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[6]>1:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[12]<=2:
							return 'True'
						elif obj[12]>2:
							return 'False'
						else: return 'False'
					elif obj[8]>1.0:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]>2:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=3:
								return 'True'
							elif obj[4]>3:
								return 'False'
							else: return 'False'
						elif obj[1]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]<=1:
					return 'True'
				else: return 'True'
			elif obj[7]>9:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[10]<=0.0:
		return 'False'
	else: return 'False'
