def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]>2:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[9]<=3.0:
			# {"feature": "Education", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[6]>0:
				# {"feature": "Age", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[12]<=2:
						# {"feature": "Gender", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[11]<=0:
									return 'True'
								elif obj[11]>0:
									return 'False'
								else: return 'False'
							elif obj[8]>1.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'False'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[12]>2:
						return 'False'
					else: return 'False'
				elif obj[4]>4:
					return 'False'
				else: return 'False'
			elif obj[6]<=0:
				return 'False'
			else: return 'False'
		elif obj[9]>3.0:
			return 'True'
		else: return 'True'
	elif obj[7]<=2:
		return 'True'
	else: return 'True'
